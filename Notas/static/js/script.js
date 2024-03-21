document.getElementById('login-form').addEventListener('submit', function(event) {
	event.preventDefault();
	var email = document.getElementById('email').value;
	var password = document.getElementById('password').value;
	// Send a request to the server to authenticate the user
	fetch('login.php', {
		method: 'POST',
		body: JSON.stringify({ email: email, password: password }),
		headers: { 'Content-Type': 'application/json' }
	})
	.then(function(response) {
		return response.json();
	})
	.then(function(data) {
		if (data.success) {
			// Redirect the user to the dashboard
			window.location.href = 'dashboard.php';
		} else {
			alert('Error: ' + data.message);
		}
	});
});