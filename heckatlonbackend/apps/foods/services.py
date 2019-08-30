import requests, json
import logging
logger = logging.getLogger("data_logger")


class DataGetterService:
    """Abstract Class for unifying data retrieval."""

    def __init__(self, serializerClass, modelClass, logit=True):
        self.serializerClass = serializerClass
        self.modelClass = modelClass

        self.logit = logit

    def create_filter_dict(self, input_dict, allowed_keys):
        """
        Create dictionary suitable for filtering queries.
        Prevents un-allowed keys and returns the error.
        """
        filterdict = {}

        for key, value in input_dict.items():
            if key not in allowed_keys:
                return None, {"error": "Invalid query parameter: %s"%key}
            key, value = FilteringService.clean(key, value)
            filterdict[key] = value
        
        return filterdict, None

    def filterit(self, filterdict, limit=10):
        """
        Fiter the modelClass query.
        """
        return self.modelClass.objects.filter(**filterdict).order_by("-updated_at")[:limit]

    def serialize(self, result_query):
        """
        Serializes the filtered result query.
        """
        return self.serializerClass(result_query, many=True)


class DataPosterService:
    """Abstract Class for unifying data posting."""

    def __init__(self, serializerClass, modelClass, logit=True):
        self.serializerClass = serializerClass
        self.modelClass = modelClass

        self.logit = logit

        self.inserted_count=0
        self.not_inserted_count=0
        self.errors=[]

    def preprocess_data(self, data):
        data = self.__normalize_data(data)
        # TODO: Maybe implement some optional preprocessing here?
        # data, _skipped = DataProcessingService.preprocess(data, self.modelClass, **kwargs)
        # self.not_inserted_count += len(_skipped)
        return data

    def insert_data(self, data):
        for obj in data:
            serializer = self.serializerClass(data=obj)
            if serializer.is_valid():
                serializer.save()
                self.inserted_count += 1
            else:
                errormessage = {
                    "object":obj,
                    "errors":serializer.errors
                }
                if self.logit:
                    logger.error("Skipped %s. %s"%(self.serializerClass.Meta.model.__name__, errormessage))
                self.not_inserted_count += 1
                self.errors.append(errormessage)

    def construct_response_data(self):
        return {
            "inserted_count": self.inserted_count,
            "skipped_count": self.not_inserted_count,
            "errors": self.errors
        }

    def __normalize_data(self, data):
        try: # If nested dict and has "data" key, take that.
            data = data.get("data", data)
        except AttributeError: # Data is already a list.
            data = data
        # Convert to list.
        data = [data] if type(data)!=list else data
        return data
