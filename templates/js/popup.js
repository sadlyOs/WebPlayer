async function createMusic(argument) {  
  const popupOverlay = document.getElementById("popupOverlay");

  const closePopup = document.getElementById("closePopup");

  const musicForm = document.getElementById("musicForm");
  
  const playlistForm = document.getElementById("playlistForm");

  const user_id = localStorage.getItem('user_id');

  const successElement = document.getElementById("success");
  console.log(argument)
  function openPopup(argument) {
    
    popupOverlay.style.display = "block";
    if (argument === "success") {
      playlistForm.style.display = "none";
    }
    else if (argument === "not_exist_playlist") {
      
      playlistForm.style.display = "block";
    }
    else {
      
      musicForm.style.display = "block";
    }
  }

  function closePopupFunc() {
    popupOverlay.style.display = "none";
    musicForm.style.display = "none";
  }

  openPopup(argument);

  closePopup.addEventListener("click", closePopupFunc);

  popupOverlay.addEventListener("click", function (event) {
    if (event.target === popupOverlay) {
      closePopupFunc();
    }
  });
  
  playlistForm.addEventListener("submit", event => {
    event.preventDefault();
    const data = new FormData(playlistForm);
    data.append("user_id", parseInt(user_id));
    postPlaylist(data).then((response) => {
      if (response.ok) return response.json()
    }).then((data) => {
      console.log(data);
      closePopupFunc();        
      playlistForm.style.display = "none";
      successElement.style.display = "block";
      openPopup("success");
    });
  })
  
  musicForm.addEventListener("submit", event => {
    console.log("Загрузка");
    musicForm.style.display = "none";
    event.preventDefault();
    const data = new FormData(musicForm);
    data.append("user_id", parseInt(user_id));
    const fileForm = new FormData();
    fileForm.append("file", data.get("file"), data.get("title"));
    fileForm.append("photo", data.get("photo"), data.get("title"));
    const response = `http://localhost:8080/music/v1/create?user_id=${data.get(
      "user_id"
    )}&title=${data.get("title")}&artist=${data.get("artist")}&album=${data.get(
      "album"
    )}&genre=${data.get("genre")}&playlist_id=${data.get("playlist_id")}`;

    const xhr = new XMLHttpRequest();

    xhr.upload.addEventListener("progress", (event) => {
      if (event.lengthComputable) {
        const BYTES_IN_MB = 1048576;
        const loadedMb = (event.loaded / BYTES_IN_MB).toFixed(1);
        const totalSizeMb = (event.total / BYTES_IN_MB).toFixed(1);
        const percentLoaded = Math.round((event.loaded / event.total) * 100);
        document.getElementById("progressBar").value = percentLoaded;
        document.getElementById(
          "uploadForm_Size"
        ).textContent = `${loadedMb} из ${totalSizeMb} МБ`;
        document.getElementById(
          "uploadForm_Status"
        ).textContent = `Загружено ${percentLoaded}% | `;
      }
    });

    xhr.addEventListener("load", (event) => {
      console.log(xhr);
      if (xhr.status === 200) {
        document.getElementById("uploadForm_Status").textContent = event.target.responseText;
        document.getElementById("progressBar").value = 0;
      } else {
        alert("Upload failed!");
      }
    });

    xhr.open("POST", response);
    xhr.setRequestHeader("accept", "application/json");

    xhr.setRequestHeader(
      "Authorization",
      `Bearer ${localStorage.getItem("token")}`
    );
    xhr.send(fileForm);
  })
  successElement.style.display = "none";
}


async function postPlaylist(data) {
  return await fetch(`http://localhost:8080/music/v1/playlist?user_id=${data.get('user_id')}&title=${data.get('title')}`, {
    method: "POST", 
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`
    },
  });
}
