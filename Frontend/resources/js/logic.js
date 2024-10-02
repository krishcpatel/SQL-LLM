api = "http://127.0.0.1:3030/"

fetch(api + "date").then(response => {
    if (!response.ok) {
        throw new Error ("Network response was not ok for getting today's date")
    }
    return response.json()
}).then(data => {
    document.getElementById("date").innerText = data.date
}).catch(error => {
    console.log('Error: ', error)
})

function submit_prompt() {
    data = {
        gmni_api_key: document.getElementById('gemini-api-key').value,
        lngchn_api_key: document.getElementById('langchain-api-key').value,
        username: document.getElementById('sql-username').value,
        password: document.getElementById('sql-pwd-key').value,
        host: document.getElementById('sql-host').value,
        port: document.getElementById('sql-port').value,
        database: document.getElementById('sql-database').value,
        prompt: document.getElementById('prompt').value
    }

    const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      }

    fetch(api + "llmresp", requestOptions).then(response => {
        if (!response.ok) {
            throw new Error ("Network response was not ok for getting llm response")
        }
        return response.json()
    }).then(data => {
        console.log(data)
        document.getElementById('llmresp').innerText = data.response
    }).catch(error => {
        console.log('Error: ', error)
    })
}