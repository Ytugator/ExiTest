import pytest
import asyncio
import grpc
import allure
from unittest.mock import AsyncMock, Mock

# Assuming we have some proto-generated gRPC modules
from service_pb2 import ChartResponse
from service_pb2_grpc import ChartServiceStub


@pytest.mark.asyncio
@allure.suite("output")
@allure.tag("WebSocket")
@allure.title("Service invalid input")
async def test_websocket_input_validation(websocket_client):
    invalid_message = "{ invalid_json }"
    await websocket_client.send(invalid_message)
    response = await websocket_client.receive()
    assert response == "Error: Malformed input."

@pytest.mark.asyncio
@allure.suite("output")
@allure.tag("gRPC")
@allure.title("Service valid output gRPC")
async def test_grpc_output_valid_request(grpc_client):
    expected_response = ChartResponse(chart_data="mock_chart")
    grpc_client.GetChart.return_value = expected_response
    response = await grpc_client.GetChart(Mock())
    assert response.chart_data == "mock_chart"


@allure.suite("Business scenario")
@allure.tag("WebSocket, gRPC")
@allure.title("Make charts")
@pytest.mark.asyncio
async def test_chart_generation_logic(websocket_client, grpc_client):
    valid_input = {"operation": "generate_chart", "data": [1, 2, 3, 4]}
    expected_chart = "Generated chart based on [1, 2, 3, 4]"
    grpc_client.GetChart.return_value = ChartResponse(chart_data=expected_chart)
    await websocket_client.send(valid_input)
    response = await grpc_client.GetChart(Mock())
    assert response.chart_data == expected_chart

@allure.suite("Business scenario")
@allure.tag("gRPC")
@allure.title("Empty data set")
@pytest.mark.asyncio
async def test_empty_dataset_chart_logic(grpc_client):
    empty_input = {"operation": "generate_chart", "data": []}
    expected_chart = "Generated chart based on []"
    grpc_client.GetChart.return_value = ChartResponse(chart_data=expected_chart)
    response = await grpc_client.GetChart(Mock())
    assert response.chart_data == expected_chart

@pytest.mark.asyncio
@allure.suite("Business scenario")
@allure.tag("gRPC, stress")
@allure.title("Large data set")
async def test_large_dataset_chart_logic(grpc_client):
    large_input = {"operation": "generate_chart", "data": list(range(10000))}
    expected_chart = "Generated chart based on large dataset"
    grpc_client.GetChart.return_value = ChartResponse(chart_data=expected_chart)
    response = await grpc_client.GetChart(Mock())
    assert response.chart_data == expected_chart
