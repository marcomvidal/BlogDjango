const gulp = require('gulp');
const imagemin = require('gulp-imagemin');
const uglify = require('gulp-uglify');
const concat = require('gulp-concat');
const minifyCss = require('gulp-minify-css');
const stripCssComments = require('gulp-strip-css-comments')

// Minificação de imagens
gulp.task('img', () =>
    gulp.src('postagens/static/src/img/*')
        .pipe(imagemin())
        .pipe(gulp.dest('postagens/static/dist/img'))
);

// Minificação e concatenação de JavaScript
gulp.task('js', () =>
    gulp.src([
        'postagens/static/src/js/jquery.js',
        'postagens/static/src/js/bootstrap.js',
        'postagens/static/src/js/clean-blog.js',
        'postagens/static/src/js/contact_me.js',
        'postagens/static/src/js/jqBootstrapValidation.js'
        ])
        .pipe(uglify())
        .pipe(concat('app.js'))
        .pipe(gulp.dest('postagens/static/dist/js'))
);

// Minificação e concatenação de CSS
gulp.task('css', () =>
    gulp.src('postagens/static/src/css/*.css')
        .pipe(stripCssComments())
        .pipe(minifyCss())
        .pipe(concat('app.css'))
        .pipe(gulp.dest('postagens/static/dist/css'))
)
