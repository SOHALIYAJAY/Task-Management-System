const editBtn = document.getElementById("editBtn");
const saveBtn = document.getElementById("saveBtn");
const inputs = document.querySelectorAll(".field input");

editBtn.onclick = () => {
    inputs.forEach(i => i.disabled = false);
    saveBtn.disabled = false;
};

saveBtn.onclick = () => {
    document.getElementById("displayName").innerText =
        document.getElementById("name").value;

    document.getElementById("displayRole").innerText =
        document.getElementById("role").value;

    inputs.forEach(i => i.disabled = true);
    saveBtn.disabled = true;
    alert("Profile Updated!");
};

document.getElementById("upload").addEventListener("change", e => {
    const file = e.target.files[0];
    if (file) {
        document.getElementById("profilePic").src =
            URL.createObjectURL(file);
    }
});
