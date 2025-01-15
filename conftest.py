import pytest
from unittest.mock import AsyncMock, Mock

@pytest.fixture
async def websocket_client():
    """Fixture for simulating a WebSocket client."""
    class MockWebSocket:
        def __init__(self):
            self.messages = []

        async def send(self, message):
            self.messages.append(message)

        async def receive(self):
            return self.messages.pop(0) if self.messages else None

    return MockWebSocket()


@pytest.fixture
async def grpc_client():
    """Fixture for simulating a gRPC client using mocks."""
    mock_channel = Mock()
    mock_stub = AsyncMock(spec=ChartServiceStub)
    return mock_stub