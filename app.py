from flask import Flask, jsonify

app = Flask(__name__)

# Sample author data with a detailed bio
author_data = {
    "author": {
        "name": "John Doe",
        "bio": """John Doe is an accomplished writer, researcher, and technology enthusiast with over two decades of experience in the field of cybersecurity, 
        artificial intelligence, and digital transformation. Having worked with some of the biggest names in the tech industry, John has played a significant role in shaping 
        discussions around data privacy, ethical AI, and security automation. His journey into the world of technology began at an early age when he started programming 
        and hacking ethical systems to understand the vulnerabilities that exist in modern networks. Over the years, he has contributed to multiple open-source security projects 
        and has been a keynote speaker at international conferences, sharing his insights on evolving cyber threats and how businesses can fortify their digital infrastructure. 
        
        John is the author of several best-selling books on cybersecurity and AI, which are widely used by professionals and students alike. His articles have been published in 
        top-tier journals and magazines, covering topics such as deep learning applications, penetration testing methodologies, and the future of AI-driven security tools. 
        In addition to his writing, John actively collaborates with universities and research organizations to develop innovative security solutions that protect against ever-growing cyber threats. 
        
        Apart from his professional endeavors, John is passionate about mentoring young talents in the tech industry, guiding them through hands-on projects and real-world cybersecurity challenges. 
        He believes that knowledge should be accessible to all and regularly conducts online courses and webinars to help individuals upskill in ethical hacking, AI security, and cloud security practices. 
        His dedication to empowering the next generation of cybersecurity professionals has earned him recognition from various industry bodies. 
        
        In his free time, John enjoys experimenting with emerging technologies, contributing to open-source projects, and writing thought-provoking blogs on the intersection of AI and security. 
        He is also an avid traveler, exploring different cultures and gaining new perspectives that inspire his work. Whether it’s analyzing complex attack vectors or simplifying intricate security 
        concepts for beginners, John remains committed to making the digital world a safer place for everyone."""
    }
}

@app.route('/author', methods=['GET'])
def get_author():
    return jsonify(author_data)

if __name__ == '__main__':
    app.run(debug=True)
