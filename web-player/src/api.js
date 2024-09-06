import axios from "axios";

export async function checkUser() {
  return await axios
    .get("http://localhost:8080/auth/v1/me", {
      headers: {
        accept: "application/json",
        Authorization: `Bearer ${localStorage.token}`,
      },
    })
    .then((response) => response)
    .then((data) => data)
    .catch((error) => error.response.status);
}

export async function authorization(username, password) {
  return await axios
    .post(
      "http://localhost:8080/auth/v1/login",
      new URLSearchParams({
        grant_type: "",
        username: username,
        password: password,
        scope: "",
        client_id: "",
        client_secret: "",
      }),
      {
        headers: {
          accept: "application/json",
        },
      }
    )
    .then((response) => response)
    .then((data) => data)
    .catch((error) => error.response);
}


export async function registration(username, email, password) {
  return await axios
    .post("http://localhost:8080/auth/v1/register", "", {
      params: {
        username: username,
        email: email,
        password: password,
      },

      headers: {
        accept: "application/json",
      },
    })
    .then((response) => response)
    .then((data) => data)
    .catch((error) => error.response);
}

export async function getUserEmail(email) {
  return await axios.get("http://localhost:8080/auth/v1/user/email", {
    params: {
      email: email,
    },
    headers: {
      accept: "application/json",
    },
  })
    .then((response) => response)
    .then((data) => data)
    .catch((error) => error.response);
}

export async function getTokenDecode(token) {
  return await axios
    .get("http://127.0.0.1:8080/auth/v1/decode_token", {
      params: {
        token: token,
      },
      headers: {
        accept: "application/json",
        "content-type": "application/x-www-form-urlencoded",
      },
    })
    .then((response) => response)
    .then((data) => data)
    .catch((error) => error.response);
}

export async function updatePassword(email, newPassword) {
  return await axios.put("http://127.0.0.1:8080/auth/v1/update_password",
    '',
    {
      params: {
        'new_password': newPassword,
        'email': email
      },
      headers: {
        'accept': 'application/json'
      }
    }
  )
    .then((response) => response)
    .then((data) => data)
    .catch((error) => error.response)
}
