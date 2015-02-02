$(document).ready ->
  $('#gender-identity-coords').gendermap().on 'mapClick', () ->
    mapData = $(@).data 'gendermap'
    $('#gender-identity-coords--male').val mapData.m
    $('#gender-identity-coords--male-quantized').val Math.ceil(mapData.m * 5)
    $('#gender-identity-coords--female').val mapData.f
    $('#gender-identity-coords--female-quantized').val Math.ceil(mapData.f * 5)

  $('#gender-expression-coords').gendermap().on 'mapClick', () ->
    mapData = $(@).data 'gendermap'
    $('#gender-expression-coords--male').val mapData.m
    $('#gender-expression-coords--male-quantized').val Math.ceil(mapData.m * 5)
    $('#gender-expression-coords--female').val mapData.f
    $('#gender-expression-coords--female-quantized').val Math.ceil(mapData.f * 5)

  $('#gender-in-furry-coords').gendermap().on 'mapClick', () ->
    mapData = $(@).data 'gendermap'
    $('#gender-in-furry-coords--male').val mapData.m
    $('#gender-in-furry-coords--male-quantized').val Math.ceil(mapData.m * 5)
    $('#gender-in-furry-coords--female').val mapData.f
    $('#gender-in-furry-coords--female-quantized').val Math.ceil(mapData.f * 5)

  # Character species/reason questions.
  currentCharacter = 1
  window.addCharacter = () ->
    $('#characters').append Handlebars.templates.character({
      characterId: currentCharacter,
      isFirst: currentCharacter is 1
    })
    currentCharacter++

  window.addCharacter()
    
