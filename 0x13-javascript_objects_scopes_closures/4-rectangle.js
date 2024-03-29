#!/usr/bin/node
// a class Rectangle that defines a rectangle:
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) && w > 0 &&
        (h = parseInt(h)) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height).split('')
      .slice(0, -1).join(''));
  }

  rotate () {
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
