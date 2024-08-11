
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

async function getMusic() {
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
      console.log(data)
      if (data.length > 0) {
        const existELement =
          document.getElementById("exist_playlist");
        existELement.style.display = "block";
        const ul = document.getElementById("playlists_ul");
        data.forEach(element => {
          console.log(element)
          let li = document.createElement(`li`);
          li.textContent = element.title;
          ul.appendChild(li);
        });
      }
      else {
        const existELement =
          document.getElementById("exist_playlist");
        existELement.style.display = "none";
      }
      

      
    });
}



getMusic();