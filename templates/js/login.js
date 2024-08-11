document
  .getElementById("loginForm")
  .addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = document.getElementById("logUsername").value;
    const password = document.getElementById("logPassword").value;
    try {
      const form = new FormData();
      form.append("username", username);
      form.append("password", password);
      console.log(form);
      const response = fetch("http://127.0.0.1:8080/auth/v1/login", {
        method: "POST",
        body: form,
      }).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
          if (response.status == 401) {
            alert("Неправильное имя пользователя или пароль, попробуйте снова");
          }
          if (response.status == 500) {
            alert("Ошибка сервера");
          }
        }
      }).then((data) => {
          console.log(data.access_token)
          localStorage.setItem("token", data.access_token);
          window.location.href = "home.html"
          alert("Вы успешно вошли!");
      });
    } catch (error) {
      console.log(error);
    }
  });
