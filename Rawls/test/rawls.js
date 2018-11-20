var Rawls = artifacts.require("./Rawls.sol");
contract("Rawls", function(accounts) {

    it("initializes with users", function() {
	return Rawls.deployed().then(function(instance) {
	    user = instance;
	    return user.users(1);
	}).then(function(candidate) {
	    assert.equal(candidate[0].toNumber(), 0, "contains correct id");
	});
    });
});
