import io

import mandolin_python_client

configuration = mandolin_python_client.Configuration(
    host = "http://localhost:8000"
)

# Enter a context with an instance of the API client
with mandolin_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mandolin_python_client.ConvertersApi(api_client)
    f = api_instance.generate_thumbnail_converter_thumbnail_post(
        '/Users/esther/Downloads/IMG_3242.jpeg',
        strategy='fit',
        color='#ff0000',
        width=200,
        height=200)
    with open('t.png', mode='wb') as p:
        p.write(f)

