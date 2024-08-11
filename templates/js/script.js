document
  .getElementById("registerForm")
  .addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = document.getElementById("regUsername").value;
    const password = document.getElementById("regPassword").value;
    const email = document.getElementById("regEmail").value;
    try {
      const response = await fetch("http://127.0.0.1:8080/auth/v1/register", {
        method: "POST",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          email: email,
          password: password,
        }),
      }).then((response) => {
        if (response.ok) {
          window.location.href = "login.html";
          return response.json();
        } else {
          if (response.status == 400) {
            throw new Error("Такой пользователь существует");
          }
          if (response.status == 500) {
            throw new Error("Ошибка сервера");
          }
        }
      });
    } catch (error) {
      alert(error);
    }
  });
