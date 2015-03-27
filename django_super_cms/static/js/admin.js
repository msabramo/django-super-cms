/**
 * Created by youngershen on 15-3-27.
 */

var login_validator = function()
{
    var value = $('#id_captcha_1').val();
    $('#re_captcha_1').remove();
    var html = "<input type='hidden' id='re_captcha_1' name='captcha_1' value='"+ value +"'>";
    $('#login_form').append(html);
    return false;
}