var switcher = 0;
function popUp( param1, param2, param3, param4, param5) {
    
    console.log( param1);
    document.querySelector('#progress-bar2').setAttribute('aria-valuenow', param1);
    document.querySelector('#progress-bar2').style.width = param1+"%";
    console.log( param2);
    document.querySelector('#harvestName').value = param2;
    console.log( param3);
    document.querySelector('#harvestArea').value = param3;
    console.log( param4);
    document.querySelector('#harvestSeedDate').value = param4;
    console.log( param5);
    document.querySelector('#harvestHarvestDate').value = param5;


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