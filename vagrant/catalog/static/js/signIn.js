(function() {

  window.renderButton = function renderButton() {
    gapi.signin2.render('login-button', {
      'clientid': '432981277858-bje89csb0so8l9d9j1lj2cv9pbhqd8r2.apps.googleusercontent.com',
      'scope': 'openid email',
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

  function hideLoginInfo() {
    const googleButton = document.getElementById('login-button');
    const googleHeader = document.getElementById('login-header');
    googleButton.style.display = 'none';
    googleHeader.style.display = 'none';
  }

  function onSuccess(result) {
    const state = getState();
    const responseDiv = document.getElementById('login-result');
    const googleButton = document.getElementById('login-button');
    const code = result['code'];
    if(code) {
      hideLoginInfo();

      return fetch( '/connect?state=' + state, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/octet-stream; charset=utf-8'
        },
        body: code,
      }).then(response => response.text()).then( (data) => {
        responseDiv.innerHTML = data;
        window.setTimeout( () => {
          window.location.href = '/topics';
        }, 3000);
      });
    }
  }

  function onFailure(err) {
    const responseDiv = document.getElementById('login-result');
    responseDiv.innerHTML = err;
  }
})();