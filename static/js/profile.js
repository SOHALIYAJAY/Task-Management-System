const editBtn = document.getElementById("editBtn");
const saveBtn = document.getElementById("saveBtn");
const inputs = document.querySelectorAll("input");

editBtn.onclick = () => {
    inputs.forEach(input => input.disabled = false);
    saveBtn.disabled = false;
};

saveBtn.onclick = () => {
    document.getElementById("displayName").innerText =
        document.getElementById("name").value;

    document.getElementById("displayRole").innerText =
        document.getElementById("role").value;

    inputs.forEach(input => input.disabled = true);
    saveBtn.disabled = true;

    alert("Profile updated successfully!");
};

/* Profile Image Preview */
document.getElementById("upload").addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        document.getElementById("profilePic").src =
            URL.createObjectURL(file);
    }
});
