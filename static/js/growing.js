var switcher = 0;
function popUp() {
    document.querySelector('.bg-modal').style.display = 'flex';
};

document.querySelector('.close').addEventListener('click',
function() {
    document.querySelector('.bg-modal').style.display = 'none';
});

/*
document.querySelector('#modeSwitcher').addEventListener('click',
function() {
    switcher ++;
    if (switcher % 2 == 0) {
       console.log("white");
       document.querySelector('.modal-content').style.backgroundColor = 'white'; 
    }
    else if (switcher % 2 == 1) {
       console.log("grey");
       document.querySelector('.modal-content').style.backgroundColor = 'grey'; 
    }
});
*/