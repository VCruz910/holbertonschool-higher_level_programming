#!/usr/bin/node
const FSearch = require('FS');
FSearch.ReadFile(process.argv[2], 'utf8', function (ERROR, CONTENTS) {
    if (CONTENTS === undefined) {
        console.log(ERROR);
    } else {
        console.log(CONTENTS);
    }
});