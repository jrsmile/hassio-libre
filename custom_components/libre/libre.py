import aiohttp
import asyncio

creds = {"email": "","password": ""}
uastring = 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.60 Mobile Safari/537.36'
headers = {
'User-Agent': uastring,
'Accept-Encoding': 'gzip',
'Cache-Control': 'no-cache',
'Connection': 'Keep-Alive',
'Content-Type': 'application/json',
'product': 'llu.android',
'version': '4.2.1',
'Accept': '*/*'
}

async def login():
    url = "https://api-de.libreview.io/llu/auth/login"
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,json=creds,headers=headers) as resp:
            if resp.status == 200:
                json_body = await resp.json()
                auth_token = json_body['data']['authTicket']['token']
                return auth_token

async def GetPatientID(AuthToken):
    url = "https://api-de.libreview.io/llu/connections"
    headers.update({'Authorization': "Bearer " + AuthToken})
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as resp:
            if resp.status == 200:
                json_body = await resp.json()
                PatientID = json_body['data'][0]['patientId']
                return PatientID

async def GetData(AuthToken,PatientID):
    url = "https://api-de.libreview.io/llu/connections/" + PatientID + "/graph"
    headers.update({'Authorization': "Bearer " + AuthToken})
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as resp:
            if resp.status == 200:
                json_body = await resp.json()
                Results = json_body['data']['connection']['glucoseMeasurement']['ValueInMgPerDl']
                return Results

if __name__ == "__main__":
    print("Login")
    AuthToken = asyncio.run(login())
    print("GetPatientID")
    PatientID = asyncio.run(GetPatientID(AuthToken=AuthToken))
    print("GetData")
    Results = asyncio.run(GetData(AuthToken=AuthToken,PatientID=PatientID))
    print(Results)
    
    