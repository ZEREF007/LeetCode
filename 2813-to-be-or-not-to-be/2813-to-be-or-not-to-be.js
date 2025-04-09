const expect = (val) => ({
    toBe: (expected) => {
        if (val === expected) {
            return true;
        } else {
            throw new Error("Not Equal");
        }
    },
    notToBe: (expected) => {
        if (val !== expected) {
            return true;
        } else {
            throw new Error("Equal");
        }
    }
});
