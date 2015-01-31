markQuestionAnswered = (number) ->
  $.getJSON "/touch/question/#{ number }", (data) ->
    if data.error
      console.error(data.error)

unlockOnOther = (name, enabled) ->
  $("input[name=#{ name }_other]").prop('disabled', not enabled)

$(document).ready ->
  $('input,textarea').on 'blur', () ->
    if $(@).data('number')
      markQuestionAnswered($(@).data('number'))

  $('input[value=other]').on 'change', () ->
    unlockOnOther($(@).attr('name'), $(@).prop('checked'))


