var gulp  = require('gulp'),
    gutil = require('gulp-util')
    exec  = require('child_process').exec
    fs    = require('fs')

gulp.task('default', () => {
    return gutil.log('Gulp is running')
})

gulp.task('auth-build', (cb) => {
    exec('sqlite3 db/data.db < src/db/auth.sql', (err, stdout, stderr) => {
        console.log(stdout);
        console.log(stderr);
        cb(err);
    })
})

gulp.task('tweet-build', ['auth-build'], (cb) => {
    exec('sqlite3 db/data.db < src/db/tweet.sql', (err, stdout, stderr) => {
        console.log(stdout);
        console.log(stderr);
        cb(err);
    })
})


gulp.task('db-clean', () => {
    fs.unlinkSync('db/data.db');
})