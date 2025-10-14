#import "Person.h"

@implementation Person

// Implementation of the greet method
- (void)greet {
    NSLog(@"Hello, my name is %@ and I am %ld years old.", self.name, (long)self.age);
}

@end
