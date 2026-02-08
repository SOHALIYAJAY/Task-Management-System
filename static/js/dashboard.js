document.addEventListener("DOMContentLoaded", () => {

    const navLinks = document.querySelectorAll(".nav-links a");
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });

    const sidebarLinks = document.querySelectorAll(".sidebar a");

    sidebarLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.parentElement.classList.add("active");
        }
    });


    const progressFill = document.querySelector(".progress-fill");

    if (progressFill) {
        const targetWidth = progressFill.style.width;
        progressFill.style.width = "0%";

        setTimeout(() => {
            progressFill.style.transition = "width 1s ease-in-out";
            progressFill.style.width = targetWidth;
        }, 200);
    }


    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = "0";
            alert.style.transform = "translateY(-10px)";
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    });

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "translateY(-4px)";
            card.style.transition = "0.2s ease";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "translateY(0)";
        });
    });

});
