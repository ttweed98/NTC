def widget(firstname, lastname, *args, **kwargs):
    print(f"My fullname is {firstname} {lastname}")
    if args:
        # print(type(args))
        print(f'I live in {args[0]} , {args[1]}, {args[2]}')
    if kwargs:
        #print(type(kwargs))
        language1 = kwargs['language1']
        print(f'I enjoy coding in  {kwargs["language1"]}')


output = (widget('Elizabeth', 'Abraham', 'ATL', 'Ga', 'USA', language1 = 'python', language2 = 'Go'))        

# output = (widget('Elizabeth', 'Abraham', language1 = 'python', language2="Go"))