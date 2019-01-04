(function() {

  window.renderButton = function renderButton() {
    gapi.signin2.render('login-button', {
      'clientid': '432981277858-bje89csb0so8l9d9j1lj2cv9pbhqd8r2.apps.googleusercontent.com',
      'scope': 'openid email profile',
      'cookiepolicy': 'single_host_origin',
      'redirecturi': 'postmessage',
      'accesstype': 'offline',
      'approvalprompt': 'force',
      'width': 240,
      'height': 50,
      'longtitle': true,
      'theme': 'dark',
      'onsuccess': onSuccess,
      'onfailure': onFailure
    });
  }   

  window.setState = function setState(newState) {
    window.state = newState;
  }

  window.getState = function getState() {
    return window.state;
  }

  function onSuccess(result) {
    const googleButton = document.getElementById('login-button');
    const state = getState();
    const responseDiv = document.getElementById('sign-in__result');
    const code = result['code'];
    if(code) {
      googleButton.style.display = 'none';

      return fetch( '/connect?state=' + state, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/octet-stream; charset=utf-8'
        },
        body: code,
      }).then(response => response.json()).then(data => responseDiv.textContent = data)
    }
  }

  function onFailure(err) {
    console.log('ERROR!----->', err);
  }
})();