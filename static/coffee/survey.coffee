markQuestionAnswered = () ->
  $.getJSON "/touch/question/#{ @data.number }", (data) ->
    if data.error
      console.error(data.error)

unlockOnOther = (name, enabled) ->
  $("input[name=#{ name }_other]").prop('disabled', not enabled)

$(document).ready ->
  $('input,textarea').blur () ->
    if @data('number')
      markQuestionAnswered(@data('number'))

  $('input[value=other]').change () ->
    unlockOnOther(@attr('name'), @prop('checked'))


