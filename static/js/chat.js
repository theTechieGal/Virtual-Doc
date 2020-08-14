/* Script to control page reloading and chat window scrolling */

$(document).ready(function() {
	var chat = document.getElementById('add');
	chat.scrollTop = chat.scrollHeight;
	setTimeout(function() {
		if (!sessionStorage.getItem("reload") && sessionStorage.getItem("notfirst")) {
			sessionStorage.setItem("reload", true);
			location.reload(true);
		}
		else
			sessionStorage.removeItem("reload");
	}, 3000);
	$('#submit').click(function() {
		sessionStorage.setItem("notfirst", true);
	});
});
