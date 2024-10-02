gmni_api_key_hidden = true
gmni_api_key_text = "Show"

lngchn_api_key_hidden = true
lngchn_api_key_text = "Show"

sql_pwd_hidden = true
sql_pwd_text = "Show"

function hide_api_gemini_key() {
    if (gmni_api_key_hidden) {
        gmni_api_key_hidden = false
        gmni_api_key_text = "Hide"
        document.getElementById("gmni-api-key-button").innerText = gmni_api_key_text
        document.getElementById("gemini-api-key").type = 'text'
    } else {
        gmni_api_key_hidden = true
        gmni_api_key_text = "Show"
        document.getElementById("gmni-api-key-button").innerText = gmni_api_key_text
        document.getElementById("gemini-api-key").type = 'password'
    }
}

function hide_api_lngchn_key() {
    if (lngchn_api_key_hidden) {
        lngchn_api_key_hidden = false
        lngchn_api_key_text = "Hide"
        document.getElementById("lngchn-api-key-button").innerText = lngchn_api_key_text
        document.getElementById("langchain-api-key").type = 'text'
    } else {
        lngchn_api_key_hidden = true
        lngchn_api_key_text = "Show"
        document.getElementById("lngchn-api-key-button").innerText = lngchn_api_key_text
        document.getElementById("langchain-api-key").type = 'password'
    }
}

function hide_sql_pwd() {
    if (sql_pwd_hidden) {
        sql_pwd_hidden = false
        sql_pwd_text = "Hide"
        document.getElementById("sql-pwd-button").innerText = sql_pwd_text
        document.getElementById("sql-pwd-key").type = 'text'
    } else {
        sql_pwd_hidden = true
        sql_pwd_text = "Show"
        document.getElementById("sql-pwd-button").innerText = sql_pwd_text
        document.getElementById("sql-pwd-key").type = 'password'
    }
}