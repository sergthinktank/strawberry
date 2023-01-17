import strawberry
from typing import AsyncGenerator


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def show_content(
        self, string: str = "Hello World"
    ) -> AsyncGenerator[str, None]:
        yield string


schema = strawberry.Schema(query=Query, subscription=Subscription)
