import axios from "axios";

export async function checkUser() {
  return axios
    .get("http://localhost:8080/auth/v1/me", {
      headers: {
        accept: "application/json",
        Authorization: `Bearer ${localStorage.token}`,
      },
    })
    .then((response) => response.json())
    .then((data) => data)
    .catch((error) => error.response.status);
}

export async function authorization(username, password) {
  return axios
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
  return axios
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
    .then((response) => {;
      return response;
    })
    .then((data) => data)
    .catch((error) => error.response);
}