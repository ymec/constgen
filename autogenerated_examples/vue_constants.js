// autogenerated by reconstant - do not edit!

// types

// constants
export const SOME_CONSTANT = "this is a constant string"
export const OTHER_CONSTANT = 42

// enums
export const SomeEnum = {
	A : 5,
	B : 6,
	C : 7,
}

SomeEnum.Mixin = {
  created () {
      this.SomeEnum = SomeEnum
  }
}
export const OtherEnum = {
	FOO : 0,
	BAR : 1,
}

OtherEnum.Mixin = {
  created () {
      this.OtherEnum = OtherEnum
  }
}
