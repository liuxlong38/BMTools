import bmtools
import os

server = bmtools.ToolServer()
print(server.list_tools())
server.load_tool("chemical-prop")
server.load_tool("douban-film")
server.load_tool("weather")
server.load_tool("wikipedia")
server.load_tool("wolframalpha")
server.load_tool("bing_search", {"subscription_key": os.getenv("BING_SUBSCRIPT_KEY", None)})
server.load_tool("office-ppt")
server.load_tool("stock", {"subscription_key": os.getenv("ALPHA_VANTAGE_KEY", None)})
server.load_tool("map", {"subscription_key": os.getenv("BING_MAP_KEY", None)})
# server.load_tool("nllb-translation")
server.load_tool("baidu-translation")
server.load_tool("tutorial")
server.serve()
