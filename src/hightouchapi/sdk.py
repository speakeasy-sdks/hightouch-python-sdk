
import requests
from . import utils
from hightouchapi.models import operations, shared
from typing import Any, Optional

SERVERS = [
	"https://api.hightouch.com/api/v1",
]


class Hightouchapi:
    

    _client: requests.Session
    _security_client: requests.Session
    
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "2.3.1"
    _gen_version: str = "1.3.2"

    def __init__(self) -> None:
        self._client = requests.Session()
        self._security_client = requests.Session()
        


    def config_server_url(self, server_url: str, params: dict[str, str]):
        if params is not None:
            self._server_url = utils.replace_parameters(server_url, params)
        else:
            self._server_url = server_url

        
    

    def config_client(self, client: requests.Session):
        self._client = client
        
    
    
    def create_destination(self, request: operations.CreateDestinationRequest) -> operations.CreateDestinationResponse:
        r"""Create Destination
        Create a new destination
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/destinations"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateDestinationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_destination_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 409:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def create_model(self, request: operations.CreateModelRequest) -> operations.CreateModelResponse:
        r"""Create Model
        Create a new model
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/models"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateModelResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_model_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 409:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def create_source(self, request: operations.CreateSourceRequest) -> operations.CreateSourceResponse:
        r"""Create Source
        Create a new source
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/sources"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateSourceResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_source_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 409:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def create_sync(self, request: operations.CreateSyncRequest) -> operations.CreateSyncResponse:
        r"""Create Sync
        Create a new sync
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/syncs"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.create_sync_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 409:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def get_destination(self, request: operations.GetDestinationRequest) -> operations.GetDestinationResponse:
        r"""Get Destination
        Retrieve a destination based on its Hightouch ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/destinations/{destinationId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDestinationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Destination])
                res.destination = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass

        return res

    def get_model(self, request: operations.GetModelRequest) -> operations.GetModelResponse:
        r"""Get Model
        Retrieve models from model ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/models/{modelId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetModelResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Model])
                res.model = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass

        return res

    def get_source(self, request: operations.GetSourceRequest) -> operations.GetSourceResponse:
        r"""Get Source
        Retrieve source from source ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/sources/{sourceId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSourceResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Source])
                res.source = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def get_sync(self, request: operations.GetSyncRequest) -> operations.GetSyncResponse:
        r"""Get Sync
        Retrieve sync from sync ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/syncs/{syncId}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Sync])
                res.sync = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass

        return res

    def list_destination(self, request: operations.ListDestinationRequest) -> operations.ListDestinationResponse:
        r"""List Destinations
        List the destinations in the user's workspace
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/destinations"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListDestinationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListDestination200ApplicationJSON])
                res.list_destination_200_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def list_model(self, request: operations.ListModelRequest) -> operations.ListModelResponse:
        r"""List Models
        List all the models in the current workspace
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/models"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListModelResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListModel200ApplicationJSON])
                res.list_model_200_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def list_source(self, request: operations.ListSourceRequest) -> operations.ListSourceResponse:
        r"""List Sources
        List all the sources in the current workspace
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/sources"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSourceResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSource200ApplicationJSON])
                res.list_source_200_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass

        return res

    def list_sync(self, request: operations.ListSyncRequest) -> operations.ListSyncResponse:
        r"""List Syncs
        List all the syncs in the current workspace
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/syncs"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSync200ApplicationJSON])
                res.list_sync_200_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def list_sync_runs(self, request: operations.ListSyncRunsRequest) -> operations.ListSyncRunsResponse:
        r"""List Sync Runs
        List all sync runs under a sync
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/syncs/{syncId}/runs", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListSyncRunsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.ListSyncRuns200ApplicationJSON])
                res.list_sync_runs_200_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def trigger_run(self, request: operations.TriggerRunRequest) -> operations.TriggerRunResponse:
        r"""Trigger Sync
        Trigger a new run for the given sync.
        
        If a run is already in progress, this queues a sync run that will get
        executed immediately after the current run completes.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/syncs/{syncId}/trigger", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.TriggerRunResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TriggerRunOutput])
                res.trigger_run_output = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def trigger_run_custom(self, request: operations.TriggerRunCustomRequest) -> operations.TriggerRunCustomResponse:
        r"""Trigger Sync From ID or Slug
        Trigger a new run globally based on sync id or sync slug
        
        If a run is already in progress, this queues a sync run that will get
        executed immediately after the current run completes.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/syncs/trigger"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.TriggerRunCustomResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.trigger_run_custom_200_application_json_any_of = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 401:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out

        return res

    def update_destination(self, request: operations.UpdateDestinationRequest) -> operations.UpdateDestinationResponse:
        r"""Update Destination
        Update an existing destination
        
        Patch a destination based on its Hightouch ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/destinations/{destinationId}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateDestinationResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_destination_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def update_model(self, request: operations.UpdateModelRequest) -> operations.UpdateModelResponse:
        r"""Update Model
        Update an existing model
        
        Patch a model based on its Hightouch ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/models/{modelId}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateModelResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_model_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def update_source(self, request: operations.UpdateSourceRequest) -> operations.UpdateSourceResponse:
        r"""Update Source
        Update an existing source
        
        Patch a source based on its Hightouch ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/sources/{sourceId}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateSourceResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_source_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    def update_sync(self, request: operations.UpdateSyncRequest) -> operations.UpdateSyncResponse:
        r"""Update Sync
        Update an existing sync
        
        Patch a sync based on its Hightouch ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/syncs/{syncId}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateSyncResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.update_sync_200_application_json_any_of = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 404:
            pass
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ValidateErrorJSON])
                res.validate_error_json = out
        elif r.status_code == 500:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.InternalServerErrorEnum])
                res.internal_server_error = out

        return res

    