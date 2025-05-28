from supraexporter.clients.rpc_client import RPCClient

client = RPCClient("http://localhost:8545/rpc/v1")  # Replace with your actual endpoint if needed

response = client.post("block")

if response:
    print("Block Height:", response.get("height"))
else:
    print("RPC call failed or returned no result.")
