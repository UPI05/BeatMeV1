var stat = new Array(20);
for (var i = 0; i < 20; i++) {
	stat[i] = new Array(20);
}
for (var i = 0; i < 20; i++) {
	for (var j = 0; j < 20; j++) stat[i][j] = 0;
}
var machineX = 0, machineY, endgame = false, waitingTime = 20000, waitSt = false;
function getMove(x, y) {
	$.ajax({
		url: 'getmove/',
		type: 'GET',
		data: {
			'raw': x,
			'col': y,
			'dt': stat
		},
		contentType: 'application/json; charset=utf-8',
		dataType: 'json',
		success: function (data) {
			console.log('ajax');
			if (data.x == 0 && data.y == 0) {
				return;
			}
			document.getElementsByClassName('p' + data.x + 'x' + data.y)[0].innerText = 'X';
			document.getElementsByClassName('p' + data.x + 'x' + data.y)[0].style.backgroundColor = 'GreenYellow';
			document.getElementsByClassName('p' + data.x + 'x' + data.y)[0].style.color = 'red';
			stat[data.x][data.y] = 2;
			machineX = data.x;
			machineY = data.y;
		},
		error: function (xhr, errmsg, err) {
			//console.log(xhr.status + ': ' + xhr.responseText);
		}
	});
	
}
function checkResult(ch) {
	for (var i = 1; i <= 19; i++) {
		for (var j = 1; j <= 19; j++) {
			if (i + 4 <= 19) {
				if (stat[i][j] == ch && stat[i][j] == stat[i + 1][j] && stat[i][j] == stat[i + 2][j] && stat[i][j] == stat[i + 3][j] && stat[i][j] == stat[i + 4][j]) return true;
			}
			if (j + 4 <= 19) {
				if (stat[i][j] == ch && stat[i][j] == stat[i][j + 1] && stat[i][j] == stat[i][j + 2] && stat[i][j] == stat[i][j + 3] && stat[i][j] == stat[i][j + 4]) return true;
			}
			if ((i + 4 <= 19) && (j + 4 <= 19)) {
				if (stat[i][j] == ch && stat[i][j] == stat[i + 1][j + 1] && stat[i][j] == stat[i + 2][j + 2] && stat[i][j] == stat[i + 3][j + 3] && stat[i][j] == stat[i + 4][j + 4]) return true;
			}
			if ((i + 4 <= 19) && (j - 4 >= 1)) {
				if (stat[i][j] == ch && stat[i][j] == stat[i + 1][j - 1] && stat[i][j] == stat[i + 2][j - 2] && stat[i][j] == stat[i + 3][j - 3] && stat[i][j] == stat[i + 4][j - 4]) return true;
			}
		}
	}
	return false;
}
function go(x, y) {
	if (endgame) {
		alert('Can\'t go! Game over.');
		return;
	}
	if (waitSt) {
		alert('Please wait for the Bot!');
		return;
	}
	if (stat[x][y] != 0) {
		alert('Can\'t go this way!');
		return;
	}
	if (machineX) {
		// If machine has gone
		document.getElementsByClassName('p' + machineX + 'x' + machineY)[0].style.backgroundColor = 'SkyBlue';
	}
	document.getElementsByClassName('p' + x + 'x' + y)[0].innerHTML = 'O';
	document.getElementsByClassName('p' + x + 'x' + y)[0].style.backgroundColor = 'GreenYellow';
	stat[x][y] = 1;
	if (checkResult(1)) {
		getMove(x, y);
		waitSt = true
		setTimeout(function () {
			console.log('js');
			ans = confirm('Congratulation... You win! Want to play again???');
			if (ans) {
				location.reload();
			} else {
				endgame = true;
			}
			waitSt = false;
		}, waitingTime);
		return;
	}
	document.getElementsByClassName('alert')[0].innerHTML = 'Waiting for machine...';
	getMove(x, y);
	waitSt = true;
	setTimeout(function () {
		console.log('js');
		document.getElementsByClassName('p' + x + 'x' + y)[0].style.backgroundColor = 'SkyBlue';
		if (checkResult(2)) {
			ans = confirm('Sorry... You lose! Want to play again???');
			if (ans) {
				location.reload();
			} else {
				endgame = true;
			}
			return;
		}
		document.getElementsByClassName('alert')[0].innerHTML = 'Your turn!';
		waitSt = false;
	}, waitingTime);
}
function setUsername() {
	var val = document.getElementsByClassName('form-control')[0].value;
	if (val == '') document.getElementsByClassName('user2')[0].innerText = 'YOU';
	else {
		if (val.length > 12) {
			document.getElementsByClassName('user2')[0].innerText = 'YOU';
			alert('Username contains from 1 to 12 characters.');
		} else document.getElementsByClassName('user2')[0].innerText = val;
	}
}