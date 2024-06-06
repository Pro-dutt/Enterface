import streamlit as st
class_names_dict = {0: 'Button', 1: 'Field', 2: 'Heading', 3: 'Iframe', 4: 'Image', 
                            5: 'Label', 6: 'Link', 7: 'Text'}
# Classes of 1st Box:
def classify(classes):
    global class_counts
    class_counts = {}
    for classCount in classes:
        class_id = int(classCount.item())
        class_name = class_names_dict[class_id]

        # Checking of classes and incrementing classes
        if class_name in class_counts:
                class_counts[class_name] += 1
        else:
            class_counts[class_name] = 1

    # Display the count and name of the classes    
    for class_name, count in class_counts.items():
        st.write(f"{class_name}: {count}")