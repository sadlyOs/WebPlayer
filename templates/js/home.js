async function sendToken() {
  const token = localStorage.getItem("token");
  try {
    const response = fetch("http://localhost:8000/auth/v1/me", {
      method: "GET",
      headers: {
        Authorization: "Bearer " + token,
      },
    })
      .then((response) => {
        if (response.ok) return response.json();

        if (response.status == 401) window.location.href = "login.html";
      })
      .then((data) => {
          document.getElementById("main").innerHTML = `Привет ${data["username"]}`;
      });
  } catch (error) {
    console.log(error);
  }
}

sendToken();
