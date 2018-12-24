(function(){
  window.renderButton = function renderButton() {
    gapi.signin2.render('login-button', {
      'scope': 'profile email',
      'width': 240,
      'height': 50,
      'longtitle': true,
      'theme': 'dark',
      'onsuccess': onSuccess,
      'onfailure': onFailure
    });
  }

  window.onSuccess = function onSuccess(user) {
    console.log('WE HAVE A USER!----->', user);
  }

  window.onFailure = function onFailure(err) {
    console.log('ERROR!----->', err);
  }
})();