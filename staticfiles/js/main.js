const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.body;
const mon = document.getElementById("mon");
const sunIcon = document.getElementById("sun");

const customTheme = (theme) => {
    const elRoot = document.documentElement;
    elRoot.setAttribute("data-theme", theme);
    localStorage.setItem('dark-mode', JSON.stringify(theme));

    if (theme === "dark") {
        mon.style.display = "none";
        sunIcon.style.display = "block";
        body.classList.add('dark-mode');
    } else {
        mon.style.display = "block";
        sunIcon.style.display = "none";
        body.classList.remove("dark-mode");
    }
};

const toggleFunction = (darkMode) => {
    if (darkMode === "dark") {
        customTheme("dark");
    } else {
        customTheme("light");
    }
};

darkModeToggle.addEventListener('click', () => {
    const darkMode = JSON.parse(localStorage.getItem('dark-mode'));
    if (darkMode === "dark") {
        toggleFunction("light");
    }else{
        toggleFunction("dark");
    }

});

const themFUnctions = ()=> {
    const darkMode = JSON.parse(localStorage.getItem('dark-mode'));
    if ( !darkMode) {
        toggleFunction("light");  
    }else{
        toggleFunction(darkMode);
    }
    

}

themFUnctions()
