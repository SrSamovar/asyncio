import asyncio
import datetime
import aiohttp
from db import add_person, create_table, drop_table


async def get_swapi_people(person_id: int, http_session):
    url = f'https://swapi.dev/api/people/{person_id}/'
    htt_response = await http_session.get(url)
    if htt_response.status == 200:
        json_data = await htt_response.json()
        return json_data
    else:
        return None


async def main():
    await create_table()
    number = 1
    none_count = 0
    async with aiohttp.ClientSession() as http_session:
        while True:
            result = await get_swapi_people(number, http_session)
            if result is None:
                none_count += 1

                if none_count > 3:
                    break
            else:
                none_count = 0
            await add_person(number, result)
            print(result)
            number += 1

    await drop_table()


if __name__ == '__main__':
    start = datetime.datetime.now()
    asyncio.run(main())
    end = datetime.datetime.now()
    print(end - start)
