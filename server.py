import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/fyhao/api/currency-exchange'

mcp = FastMCP('currency-exchange')

@mcp.tool()
def listquotes() -> dict: 
    '''List the available quotes in JSON Array this API support, all the available quotes can be used in source and destination quote. Refer exchange endpoint for more information how to call the currency exchange from the source quote to destination quote.'''
    url = 'https://currency-exchange.p.rapidapi.com/listquotes'
    headers = {'x-rapidapi-host': 'currency-exchange.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exchange(_from: Annotated[str, Field(description='Source Quote')],
             to: Annotated[str, Field(description='Destination Quote')],
             q: Annotated[Union[int, float, None], Field(description='Source Amount Default: 1')] = None) -> dict: 
    '''Get Currency Exchange by specifying the quotes of source (from) and destination (to), and optionally the source amount to calculate which to get the destination amount, by default the source amount will be 1.'''
    url = 'https://currency-exchange.p.rapidapi.com/exchange'
    headers = {'x-rapidapi-host': 'currency-exchange.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
