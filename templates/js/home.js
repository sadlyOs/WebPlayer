
document.addEventListener('DOMContentLoaded', () => {
  const token = localStorage.getItem("token");
  try {
    const response = fetch("http://localhost:8080/auth/v1/me", {
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
        document.getElementById(
          "welcome"
        ).innerHTML = `Привет ${data["username"]}`;
        localStorage.setItem("user_id", data["sub"]);
      });
  } catch (error) {
    console.log(error);
  }
})

document.addEventListener('DOMContentLoaded', () => {
  const user_id = localStorage.getItem("user_id");
  const token = localStorage.getItem("token");
  const response = fetch(
    `http://localhost:8080/music/v1/allPlaylists?user_id=${user_id}`,
    {
      method: "GET",
      headers: {
        Authorization: "Bearer " + token,
      },
    }
  )
    .then((response) => {
      if (response.ok) return response.json();
    })
    .then((data) => {
      console.log(data);
      if (data.length > 0) {
        const existELement = document.getElementById("exist_playlist");
        existELement.style.display = "block";

        let conteiner = document.getElementById("content_conteiner");
        for (let index = 0; index < data.length; index++) {
          let newDiv = document.createElement("div");
          const link = data[index].photo_path.replace(/\s/g, "+");
          newDiv.className = "conteiner__show__playlists";
          newDiv.id = "conteiner__show_playlists";
          newDiv.innerHTML = `
          <img src=${link}>
          <p class="album">${data[index].title}</p>
          `;
          conteiner.appendChild(newDiv);
        }
      } else {
        const existELement = document.getElementById("exist_playlist");
        existELement.style.display = "none";
      }
    });

});


window.onload = (event) => {
  console.log("load")
  document
    .getElementById("conteiner__show_playlists")
    .addEventListener("click", (event) => {
      console.log(event);
    });
}
// document
//   .getElementById("conteiner__show_playlists")
//   .addEventListener("click", (event) => {
//     console.log(event);
//   });