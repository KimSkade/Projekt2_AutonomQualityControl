from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.procedure import Procedure
from ...models.put_item_quality_data_aas_item_id_procedure_put_response_put_item_qualitydataaas_item_id_procedure_put import (
    PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut,
)
from ...types import Response


def _get_kwargs(
    item_id: str,
    *,
    client: Client,
    json_body: Procedure,
) -> Dict[str, Any]:
    url = "{}/QualityDataAAS/{item_id}/Procedure/".format(client.base_url, item_id=item_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: Client,
    json_body: Procedure,
) -> Response[
    Union[
        Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut
    ]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (Procedure):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: Client,
    json_body: Procedure,
) -> Optional[
    Union[
        Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut
    ]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (Procedure):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: Client,
    json_body: Procedure,
) -> Response[
    Union[
        Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut
    ]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (Procedure):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: Client,
    json_body: Procedure,
) -> Optional[
    Union[
        Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut
    ]
]:
    """Put Item

    Args:
        item_id (str):
        json_body (Procedure):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, PutItemQualityDataAASItemIdProcedurePutResponsePutItemQualitydataaasItemIdProcedurePut]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
