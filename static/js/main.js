/**
 * TürkiyeGPT - Main JavaScript
 * Global JavaScript functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId !== '#') {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Add active class to current nav link
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Example card click animation
    const exampleCards = document.querySelectorAll('.example-card');
    exampleCards.forEach(card => {
        card.addEventListener('click', function() {
            // Could redirect to chat page with pre-filled question
            const question = this.querySelector('p').textContent;
            sessionStorage.setItem('prefilled-question', question);
            window.location.href = '/chat';
        });
    });

    // Check for prefilled question on chat page
    if (window.location.pathname === '/chat') {
        const prefilledQuestion = sessionStorage.getItem('prefilled-question');
        if (prefilledQuestion) {
            const messageInput = document.getElementById('messageInput');
            if (messageInput) {
                messageInput.value = prefilledQuestion;
                messageInput.focus();
            }
            sessionStorage.removeItem('prefilled-question');
        }
    }

    // Mobile menu toggle (for future mobile nav implementation)
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    if (mobileMenuButton) {
        mobileMenuButton.addEventListener('click', function() {
            const navMenu = document.querySelector('.nav-menu');
            navMenu.classList.toggle('active');
        });
    }

    // Add scroll effect to navbar
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > lastScroll && currentScroll > 100) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });

    // Add fade-in animation to elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe feature cards and example cards
    const animatedElements = document.querySelectorAll('.feature-card, .example-card, .about-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    console.log('🚀 TürkiyeGPT loaded successfully!');
});

// Mesaj formatını temizle ve düzenle
function formatMessage(message) {
    // Markdown formatlarını temizle
    let formatted = message
        .replace(/### /g, '')  // ### başlıkları kaldır
        .replace(/\*\*(.*?)\*\*/g, '$1')  // **kalın** yazıları düz metin yap
        .replace(/\*(.*?)\*/g, '$1')  // *italik* yazıları düz metin yap
        .replace(/`(.*?)`/g, '$1')  // `kod` bloklarını düz metin yap
        .replace(/#{1,6} /g, '')  // Tüm başlık işaretlerini kaldır
        .replace(/---+/g, '')  // Çizgileri kaldır
        .replace(/\n{3,}/g, '\n\n');  // Çoklu satır sonlarını tek yap
    
    return formatted;
}

// Utility function to show notifications (can be used in future)
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'error' ? '#ef4444' : type === 'success' ? '#10b981' : '#3b82f6'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 9999;
        animation: slideInRight 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Add CSS for notification animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

