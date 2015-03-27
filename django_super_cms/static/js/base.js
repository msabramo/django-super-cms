/**
 * Created by youngershen on 15-3-26.
 */

$('.js-captcha-refresh').click(function(){

    var refresh_url = $('#captcha_refresh_url').attr('value');

    $.getJSON(refresh_url, {}, function(json) {
        $('#id_captcha_0').attr('value', json.key);
        $('#captcha_image').attr('src', json.image_url);
        $('#id_captcha_1').attr('name', json.key);
    });

    return false;
});

var reset_login_form = function()
{
    $('#username').val('');
    $('#password').val('');
    $('#id_captcha_1').val('');
    $('#password_confirm').val('');
}
