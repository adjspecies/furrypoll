(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['character'] = template({"1":function(depth0,helpers,partials,data) {
  return " checked=\"checked\"";
  },"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "<!-- Character -->\n<div class=\"character\" data-characternumber=\""
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "\">\n    <h3>Character #"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "</h3>\n    <h4>What species is this character? (If this character is a hybrid, check all that apply)</h4>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"wolf\" type=\"checkbox\"> Canine, Wolf</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"redfox\" type=\"checkbox\"> Canine, Fox, Red</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"greyfox\" type=\"checkbox\"> Canine, Fox, Grey</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"arcticfox\" type=\"checkbox\"> Canine, Fox, Arctic</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"kitsune\" type=\"checkbox\"> Canine, Fox, Kitsune</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"fennec\" type=\"checkbox\"> Canine, Fox, Fennec</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherfox\" type=\"checkbox\"> Canine, Fox, Other/Nonspecific</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"coyote\" type=\"checkbox\"> Canine, Coyote</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"jackal\" type=\"checkbox\"> Canine, Jackal</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"germanshepherd\" type=\"checkbox\"> Canine, Dog, German shepherd</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"husky\" type=\"checkbox\"> Canine, Dog, Husky</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"collie\" type=\"checkbox\"> Canine, Dog, Collie</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherdog\" type=\"checkbox\"> Canine, Dog, Other/Nonspecific</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"othercanine\" type=\"checkbox\"> Canine, Other/Nonspecific</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"tiger\" type=\"checkbox\"> Feline, Tiger</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"lion\" type=\"checkbox\"> Feline, Lion</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"leopard\" type=\"checkbox\"> Feline, Leopard</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"snowleopard\" type=\"checkbox\"> Feline, Snow leopard</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"panther\" type=\"checkbox\"> Feline, Panther</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"cheetah\" type=\"checkbox\"> Feline, Cheetah</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"cougar\" type=\"checkbox\"> Feline, Cougar</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"domesticcat\" type=\"checkbox\"> Feline, Domestic cat</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherfeline\" type=\"checkbox\"> Feline, Other/Nonspecific</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"dragon\" type=\"checkbox\"> Reptiloid, Dragon</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"lizard\" type=\"checkbox\"> Reptiloid, Lizard</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"dinosaur\" type=\"checkbox\"> Reptiloid, Dinosaur</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherreptile\" type=\"checkbox\"> Reptiloid, Other/Nonspecific</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"raccoon\" type=\"checkbox\"> Musteloid, Raccoon</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"skunk\" type=\"checkbox\"> Musteloid, Skunk</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"badger\" type=\"checkbox\"> Musteloid, Badger</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"riverotter\" type=\"checkbox\"> Musteloid, Otter, River</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"seaotter\" type=\"checkbox\"> Musteloid, Otter, Sea</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"weasel\" type=\"checkbox\"> Musteloid, Weasel</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"othermustelid\" type=\"checkbox\"> Musteloid, Other mustelid</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"redpanda\" type=\"checkbox\"> Musteloid, Red Panda</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"othermusteloid\" type=\"checkbox\"> Musteloid, Other/Nonspecific</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"horse\" type=\"checkbox\"> Ungulate, Horse</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"deer\" type=\"checkbox\"> Ungulate, Deer</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherungulate\" type=\"checkbox\"> Ungulate, Other</label>      \n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"brownbear\" type=\"checkbox\"> Bear, Brown</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"grizzlybear\" type=\"checkbox\"> Bear, Grizzly</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"pandabear\" type=\"checkbox\"> Bear, Panda</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"polarbear\" type=\"checkbox\"> Bear, Polar</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherbear\" type=\"checkbox\"> Bear, Other/Nonspecific</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"mouse\" type=\"checkbox\"> Rodent, Mouse</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"rat\" type=\"checkbox\"> Rodent, Rat</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"squirrel\" type=\"checkbox\"> Rodent, Squirrel</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"other\" type=\"checkbox\"> Rodent, Other/Nonspecific</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"raven\" type=\"checkbox\"> Bird, Raven/Crow</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"raptor\" type=\"checkbox\"> Bird, Bird of Prey</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherbird\" type=\"checkbox\"> Bird, Other</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"rabbit\" type=\"checkbox\"> Rabbit/Hare</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"kangaroo\" type=\"checkbox\"> Kangaroo</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"koala\" type=\"checkbox\"> Koala</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"othermarsupial\" type=\"checkbox\"> Other Marsupial</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"lemur\" type=\"checkbox\"> Lemur</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"monkey\" type=\"checkbox\"> Monkey</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"otherprimate\" type=\"checkbox\"> Other Primate</label>\n    </div>\n    <div class=\"species-block\">\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"hyaena\" type=\"checkbox\"> Hyena</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"bat\" type=\"checkbox\"> Bat</label>\n        <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"griffin\" type=\"checkbox\"> Griffin</label>\n    </div>\n    <br clear=\"all\" />\n    <label class=\"checkbox\"><input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_category\" value=\"other\" type=\"checkbox\"> Other</label>\n    <p>\n        Optionally, enter your own species text:</label>\n        <input name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_species\" type=\"text\" size=\"36\">\n    </p>\n    <h4>What is the reason you chose this/these species for this character?</h4>\n    <textarea name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_reason\"></textarea></label>\n    <label class=\"checkbox\"><input type=\"checkbox\" name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_primary\"";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.isFirst : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + " /> This is my primary character.</label>\n    <label class=\"checkbox\"><input type=\"checkbox\" name=\"chr_"
    + escapeExpression(((helper = (helper = helpers.characterId || (depth0 != null ? depth0.characterId : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"characterId","hash":{},"data":data}) : helper)))
    + "_deprecated\" /> I no longer identify as this character.\n</div>\n";
},"useData":true});
})();